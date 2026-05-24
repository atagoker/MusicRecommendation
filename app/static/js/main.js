const form = document.getElementById('recommendation-form');
const recommendationList = document.getElementById('recommendation-list');
const recommendButton = document.getElementById('recommend-button');
const songInputs = [
    document.getElementById('song-1'),
    document.getElementById('song-2'),
    document.getElementById('song-3'),
].filter(Boolean);

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

function renderError(message = 'Something went wrong.') {
    recommendationList.innerHTML = `
        <article class="empty-state error">
            <strong>${escapeHtml(message)}</strong>
            <span>Enter all three songs and try again.</span>
        </article>
    `;
}

function renderRecommendation(data) {
    const track = data.recommendations[0];
    const matched = data.matched_inputs
        .map((item) => `${escapeHtml(item.title)} - ${escapeHtml(item.artist)}`)
        .join(', ');

    recommendationList.innerHTML = `
        <article class="track-card feature-card">
            <div class="track-rank">${track.match_score}% match</div>
            <div class="track-info">
                <h3>${escapeHtml(track.title)}</h3>
                <p>${escapeHtml(track.artist)}</p>
                <span>${escapeHtml(track.why)}</span>
            </div>
            <div class="match-meta">
                <span>Selected from a ${data.catalog_size}-track local catalog</span>
                <span>Matched inputs: ${matched || 'catalog defaults'}</span>
            </div>
            <a href="${track.spotify_url}" target="_blank" rel="noopener noreferrer" aria-label="Open ${escapeHtml(track.title)} on Spotify">
                Open on Spotify
            </a>
        </article>
    `;
}

async function fetchRecommendation(event) {
    event.preventDefault();

    const songs = songInputs.map((input) => input.value.trim());
    if (songs.some((song) => !song)) {
        renderError('Please enter all 3 songs.');
        return;
    }

    recommendButton.disabled = true;
    recommendButton.classList.add('loading');
    recommendationList.innerHTML = `
        <article class="empty-state">
            <strong>Scanning the catalog...</strong>
            <span>Comparing genre, mood, energy, and danceability.</span>
        </article>
    `;

    try {
        const response = await fetch('/api/recommendations', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ songs }),
        });
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || 'Recommendation request failed');
        }
        renderRecommendation(data);
    } catch (error) {
        console.error('Error:', error);
        renderError(error.message);
    } finally {
        recommendButton.disabled = false;
        recommendButton.classList.remove('loading');
    }
}

if (form) {
    form.addEventListener('submit', fetchRecommendation);
}

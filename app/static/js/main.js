document.getElementById('recommendation-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const userId = document.getElementById('user_id').value;
    fetch(`/recommend/${userId}`)
        .then(response => response.json())
        .then(data => {
            const recommendationList = document.getElementById('recommendation-list');
            recommendationList.innerHTML = '';
            data.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = `Item ${item}`;
                recommendationList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error:', error));
});

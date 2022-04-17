function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId })
    }).then((_res) => {
        window.location.href = "/notes";
    });
}

function deleteReview(gameId, reviewId) {
    fetch('/delete-review', {
        method: 'POST',
        body: JSON.stringify({ reviewId: reviewId })
    }).then((_res) => {
        window.location.href = "/games/" + gameId.toString();
    });
}

function addToLibrary(gameId) {
    fetch('/add-to-library', {
        method: 'POST',
        body: JSON.stringify({ gameId: gameId })
    }).then((_res) => {
        window.location.href = "/games/" + gameId.toString();
    });
}
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

function deleteComplaint(complaintId) {
    fetch('/delete-complaint', {
        method: 'POST',
        body: JSON.stringify({ complaintId: complaintId })
    }).then((_res) => {
        window.location.href = "/complaints";
    });
}

function checkComplaint(complaintId) {
    fetch('/check-complaint', {
        method: 'POST',
        body: JSON.stringify({ complaintId: complaintId })
    }).then((_res) => {
        window.location.href = "/complaints/manage";
    });
}

function uncheckComplaint(complaintId) {
    fetch('/uncheck-complaint', {
        method: 'POST',
        body: JSON.stringify({ complaintId: complaintId })
    }).then((_res) => {
        window.location.href = "/complaints/manage";
    });
}

function deleteUpload(uploadId) {
    fetch('/delete-upload', {
        method: 'POST',
        body: JSON.stringify({ uploadId: uploadId })
    }).then((_res) => {
        window.location.href = "/uploads/manage";
    });
}

function deleteScreenshot(gameId, uploadId) {
    fetch('/delete-screenshot', {
        method: 'POST',
        body: JSON.stringify({ uploadId: uploadId })
    }).then((_res) => {
        window.location.href = "/library/" + gameId;
    });
}
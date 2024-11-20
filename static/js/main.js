document.addEventListener('DOMContentLoaded', function () {
	document.getElementById('year').textContent =
		new Date().getFullYear() +
		'© Jipange. Made for those who value their time.';

	document.getElementById('showSignup').addEventListener('click', function () {
		var loginModal = bootstrap.Modal.getInstance(
			document.getElementById('loginModal')
		);
		loginModal.hide();
		var signupModal = new bootstrap.Modal(
			document.getElementById('signupModal')
		);
		signupModal.show();
	});

	document.getElementById('showLogin').addEventListener('click', function () {
		var signupModal = bootstrap.Modal.getInstance(
			document.getElementById('signupModal')
		);
		signupModal.hide();
		var loginModal = new bootstrap.Modal(document.getElementById('loginModal'));
		loginModal.show();
	});
});

// const LOCAL_STORAGE_KEY = 'anonymous_notes';

// // Save notes to localStorage with an expiry time
// function saveNotesToLocal(notes) {
// 	const now = new Date();
// 	const expiryTime = now.getTime() + 24 * 60 * 60 * 1000; // 1 day in milliseconds
// 	const data = { notes, expiry: expiryTime };
// 	localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(data));
// }

// // Fetch notes from localStorage
// function getNotesFromLocal() {
// 	const data = localStorage.getItem(LOCAL_STORAGE_KEY);
// 	if (data) {
// 		try {
// 			const parsed = JSON.parse(data);
// 			const now = new Date();
// 			if (now.getTime() < parsed.expiry) {
// 				return parsed.notes || [];
// 			} else {
// 				// Expired data, clear from localStorage
// 				localStorage.removeItem(LOCAL_STORAGE_KEY);
// 			}
// 		} catch (error) {
// 			console.error('Error parsing localStorage data:', error);
// 			localStorage.removeItem(LOCAL_STORAGE_KEY);
// 		}
// 	}
// 	return [];
// }

// // Add a new note to the local storage
// function addNoteToLocal(title, content, dueDate) {
// 	const notes = getNotesFromLocal();
// 	const newNote = {
// 		title,
// 		content,
// 		due_date: dueDate || 'No due date',
// 		created_at: new Date().toISOString(),
// 	};
// 	notes.push(newNote);
// 	saveNotesToLocal(notes);
// }

// // Render notes dynamically for unauthenticated users
// function renderNotes() {
// 	const notes = getNotesFromLocal();
// 	const notesList = document.getElementById('notes-list');
// 	notesList.innerHTML = ''; // Clear current content

// 	if (notes.length > 0) {
// 		notes.forEach((note) => {
// 			const noteDiv = document.createElement('div');
// 			noteDiv.className = 'note list-group-item';
// 			noteDiv.innerHTML = `
//                     <h5 class="mb-1">${note.title}</h5>
//                     <p class="mb-1">${note.content}</p>
//                     <small>Due: ${note.due_date}</small>
//                 `;
// 			notesList.appendChild(noteDiv);
// 		});
// 	} else {
// 		notesList.innerHTML = '<p>No notes found in local storage.</p>';
// 	}
// }

// // Initialize
// document.addEventListener('DOMContentLoaded', () => {
// 	renderNotes();

// 	// Example of adding a new note (can be replaced with actual form submission)
// 	document.getElementById('addNoteButton')?.addEventListener('click', () => {
// 		const title = prompt('Enter note title:');
// 		const content = prompt('Enter note content:');
// 		const dueDate = prompt('Enter due date (optional):');
// 		addNoteToLocal(title, content, dueDate);
// 		renderNotes();
// 	});
// });

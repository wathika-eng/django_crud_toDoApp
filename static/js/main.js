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

// Import the functions you need from the SDKs
import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyDc7bBhMvnN84gd0--jNkyFsDa690N9KGw",
    authDomain: "digitalmemory-fbe68.firebaseapp.com",
    projectId: "digitalmemory-fbe68",
    storageBucket: "digitalmemory-fbe68.appspot.com",
    messagingSenderId: "1040826402889",
    appId: "1:1040826402889:web:723a7a175be090f1275798"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Sign up function
function signUp() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            alert('User signed up successfully!');
        })
        .catch((error) => {
            alert(error.message);
        });
}

// Sign in function
function signIn() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            const user = userCredential.user;
            alert('User signed in successfully!');
        })
        .catch((error) => {
            alert(error.message);
        });
}

// Export functions to use them in HTML
export { signUp, signIn };

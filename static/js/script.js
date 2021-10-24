$(()=>{
    const firebaseConfig = {
        apiKey: "AIzaSyCYXRlN1J3LNHW1s0vE4OPwAyGG0pv1RyA",
        authDomain: "nokhik.firebaseapp.com",
        projectId: "nokhik",
        storageBucket: "nokhik.appspot.com",
        messagingSenderId: "108976871596",
        appId: "1:108976871596:web:57b78ac86862c2624b2709",
        measurementId: "G-6251J3TWSE"
    };
    const firebaseApp = firebase.initializeApp(firebaseConfig);
    const db = firebaseApp.firestore();
    const push=(a)=>{
        db.collection('dic').add({
            word:a
        })
    }
    // push('内藤剛汰')
})
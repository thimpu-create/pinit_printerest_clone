// show/close board Modal

console.log("connected")
const createBoardBtn = document.querySelector("#createBoardBtn");
const modal = document.querySelector("#simpleModal");
const edit_pin = document.getElementById("editPinBtn")
const cancle_pin = document.getElementById("cancle-btn");
const editFormModal = document.getElementById("editPinForm") // selecting the modal


// edit_pin.



edit_pin.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("clicked",editFormModal)
  editFormModal.style.display = "block";
});

//cancle edit
cancle_pin.addEventListener("click", (e) => {
  e.preventDefault();
  editFormModal.style.display = "none";
});


// createBoardBtn.addEventListener("click", (e) => {
//   e.preventDefault();
//   modal.style.display = "block";

// });

window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.style.display = "none";
  }
});








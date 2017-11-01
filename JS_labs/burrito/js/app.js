$('.ui.checkbox').checkbox();

// $('.ui.checkbox').click(function () {
//     var box = $(this).children();
//     if (box[0].checked === true) {
//         console.log("True")
//     } else {
//         console.log("False")
//     }
// });

console.log($('.ui.checkbox'));

$('.ui.checkbox input').change(function () {
    console.log("Hi, Nick.");
   if (this.checked === true) {
       console.log("True")
   } else {
       console.log("False")
   }
});

// console.log($("[name='extra-ingredients']"));
//
// console.log();
//
// $('[value="guacamole"]').click(function () {
//     if (this.checked === true) {
//         console.log("True")
//     } else {
//         console.log("False")
//     }
// });


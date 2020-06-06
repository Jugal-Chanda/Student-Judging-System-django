$('.subject_add_icon').click(function() {
  $('#add_subject_model').modal('show');
});

$('.chapter_add_icon').click(function() {
  $('#add_chapter_model').modal('show');
});


// function chapter_clicked() {
//
// }


$('.back_icon').click(function(){
  $('#subject_card').css('display','block');
  $('#chapter_card').css('display','none');
});

$('.add_student_div').click(function(){
  $('#add_student_model').modal('show');
});

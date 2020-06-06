$('.subject_add_icon').click(function() {
  $('#add_subject_model').modal('show');
});

$('.chapter_add_icon').click(function() {
  $('#add_chapter_model').modal('show');
});


// function chapter_clicked() {
//
// }

$('#add_rating_btn').click(function(){
  $('#add_mark_model').modal('show');
})

$('.back_icon').click(function(){
  $('#subject_card').css('display','block');
  $('#chapter_card').css('display','none');
});

$('.add_student_div').click(function(){
  $('#add_student_model').modal('show');
});

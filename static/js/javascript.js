$("#student_table").on("click", "tr", function(event){
    console.log(event);
    console.log($(this).attr('data-student-id'));
    id = $(this).attr('data-student-id');
    location.replace("/profile/"+id);
});

$('.subject_add_icon').click(function() {
  $('#add_subject_model').modal('show');
});

$('.chapter_add_icon').click(function() {
  $('#add_chapter_model').modal('show');
});

$('#chahpter_table').on("click", "tr", function(event){
  id = $(this).attr('data-chapter-id');
  $('#add_rating_btn2').attr('data-chapter-id',id);
  $('#add_mark_model').modal('show');
});

$('.back_icon').click(function(){
  $('#subject_card').css('display','block');
  $('#chapter_card').css('display','none');
});

$('.add_student_div').click(function(){
  $('#add_student_model').modal('show');
});

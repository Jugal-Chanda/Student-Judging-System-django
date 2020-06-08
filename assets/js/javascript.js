$("#student_table").on("click", "tr", function(event){
    console.log(event);
    console.log($(this).attr('data-student-id'));
    id = $(this).attr('data-student-id');
    location.replace("/profile/"+id);
});

// Add new student ajax submit
$('#add_student_submit_btn').click(function() {
  url = $(this).attr('data-action-url')
  image = document.getElementById('student_image').files[0];
  name = $('input[name = student_name]').val();
  email = $('input[name = student_email]').val();
  phone = $('input[name = student_phone]').val();
  formData = new FormData();
  formData.append('image',image);
  formData.append('fullname',name);
  formData.append('email',email);
  formData.append('phone',phone);
  formData.append('csrfmiddlewaretoken',$('input[name = csrfmiddlewaretoken]').val());
  $.ajax({
    url: url,
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (data) {
      console.log(data.image);

      // markup = '<tr scope="row" data-student-id="'+ data.id + '"class="students_row">';
      // markup += '<td><img src="/media/' + data.image + '" alt="" class="student_img_table"></td>';
      // markup += '<td>' +  data.fullname +'</td>';
      // markup += '<td>' +  data.email +'</td>';
      // markup += '<td>' +  data.phone +'</td>';
      // markup += '<td>' +  '0.0' +'</td>';
      // markup += '</tr>';
      //
      // tableBody = $("#student_table");
      // tableBody.append(markup);
      $('#add_student_model').modal('hide');
    }
  });
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

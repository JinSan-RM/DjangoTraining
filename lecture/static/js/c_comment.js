$(function(){ //onload function - 모두 로드 되었을 때
    $('#comment_create_btn').on('click',function() {    //comment_create_btn 버튼이 클릭 되었을 때 실행 함수
        $.ajax({
            async:true, //비동기 방식으로 ajax호출
            url : '/bbs/commentCreate/',
            type: 'GET', //서버에 전송할 데이터
            data:{
                board_id : $('#board_id').text(),
                user_name : $('#c_name').val(),
                user_content : $('#c_content').val()

            },
            dataType : 'json', // 요청 후 서버로 부터 받을 데이터 형식
            //만약 성공하면
            success : function(result){
                let tr = $("<tr></tr>")
                let author_td = $("<td></td>").text(result.comment_author)
                let content_td = $("<td></td>").text(result.comment_content)
                let delete_td = $("<td></td>").text('삭제버튼')
                tr.append(author_td)
                tr.append(content_td)
                tr.append(delete_td)

                $('tbody').preprend(tr)
            },

            error : function(){
                alert('에러입니다.')
            }
        })
    })
})
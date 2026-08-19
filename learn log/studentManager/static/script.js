document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('.edit-btn').forEach(btn => {
        btn.addEventListener('click',function(){
            const row = this.closest('tr')

            row.querySelector('.score-text').style.display = 'none';
            row.querySelector('.score-input').style.display = 'inline-block';
            this.style.display = 'none';
            row.querySelector('.save-btn').style.display = 'inline-block';
            row.querySelector('.cancel-btn').style.display = 'inline-block';
        });
    });
    
    document.querySelectorAll('.save-btn').forEach(btn => {
        btn.addEventListener('click',function(){
            const row = this.closest('tr');
            const url = this.dataset.url;
            const scoreInput = row.querySelector('.score-input');
            const newScore = parseFloat(scoreInput.value);

            if(isNaN(newScore) || newScore < 0 || newScore > 100){
                alert("成绩必须是0-100的数字")
                return ;
            }

            fetch(url,{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({score:newScore})
            })
            .then(response => response.json())
            .then(data => {
                if(data.success){
                    row.querySelector('.score-text').textContent = data.new_score;

                    row.querySelector('.score-text').style.display = 'inline';
                    row.querySelector('.score-input').style.display = 'none';
                    row.querySelector('.edit-btn').style.display = 'inline-block';
                    row.querySelector('.save-btn').style.display = 'none';
                    row.querySelector('.cancel-btn').style.display = 'none';
                }else{
                    alert('修改失败:' + data.message);
                }
            })
            .catch(error => {
                alert('网络错误，修改失败');
                console.error('Error:',error);
            });
        });
    });
    document.querySelectorAll('.cancel-btn').forEach(btn => {
        btn.addEventListener('click',function(){
            const row = this.closest('tr');
            row.querySelector('.score-text').style.display = 'inline';
            row.querySelector('.score-input').style.display = 'none';
            row.querySelector('.edit-btn').style.display = 'inline-block';
            row.querySelector('.save-btn').style.display = 'none';
            row.querySelector('.cancel-btn').style.display = 'none';

            const originalScore = row.querySelector('.score-text').textContent;
            row.querySelector('.score-input').value = originalScore;
        });
    });
});
let namebox=document.querySelector("#nbox");
let photobox=document.querySelector("#photo");


//得到人物初始数据
function getperson_raw(){
    var resp_data;
    $.ajax({
        "url":"/getone",
        async:false,
        type:"get",
        success:function(resp){
            resp_data=resp;
        }
    })
    console.log(resp_data);
    return resp_data;
}

//下一个
function openindex(args){
    resp_data=getperson_raw();
    _person=resp_data.person;
    has_photo=resp_data.has_photo;
      photobox.setAttribute("src", resp_data.photo);
      namebox.innerHTML=_person;

}

//pio plugin start
var pio = new Paul_Pio({
    "mode": "fixed",
    "hidden": false,
    "content": {
        "welcome": ["欢迎使用抽奖小程序！", "今天会抽到谁呢~"],
        "custom": [
            {"selector": ".comment-form", "text": "欢迎参与本文评论，别发小广告噢~"},
            {"selector": ".home-social a:last-child", "text": "在这里可以了解博主的日常噢~"},
            {"selector": ".post-item a", "type": "read"},
            {"selector": ".post-content a, .page-content a", "type": "link"}
        ]
    },
    "night": "single.night()",
    "model": ["./assets/Pio-master/models/lightningyayi/model.json"]
});
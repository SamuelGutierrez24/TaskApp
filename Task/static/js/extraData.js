class countC{
    static count = 0;
    constructor(){
      this.instanceId = ++countC.count;
    }

}

function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    console.log(newElement)
    var a = new countC();
    var total = newElement.attr('id').replace("d_", "");
    total = parseInt(total)
    var newId = 'd_'+(total+1);

    newElement.find(':input').each(function() {
        var name = $(this).attr('name');
        var id = ('id_' + name).replace('0', total);
        if($(this).attr('type') === 'button'){
            $(this).attr({'name': name, 'id': id, 'data-div':newId, style:'visibility:visible'});
        }
        else{
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        }
        
    });
    var oldId = 't_'+(total);

    newElement.attr({'id': newId});
    try{
        newElement.find("#d_" + (total)).attr({'id':"d_" + (total+1)});
        newElement.find("#d_"+(total+1)).text(total+2);
        console.log(newElement.find("#d_"+(total+1)));
    }
    catch (e){
        console.log(e); 
    }
    
    $('div.extra:last').after(newElement);
    
}
function deleteMyself(id){
    $(id).remove();
}



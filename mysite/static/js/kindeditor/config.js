KindEditor.ready(function(K) {
                K.create('textarea[name=content]',{
                    width:'100%',
                    height:'400px',
                    uploadJson: '/admin/upload',
                });
        });


window.onload = function () {
            new QWebChannel(qt.webChannelTransport, function (channel) {
                // 获取qt中绑定的交互对象
                window.pyjs = channel.objects.interact_obj

                // js 绑定qt中的信号
                pyjs.sig_send_to_js.connect(function (str) {
                    document.getElementById("output").value = str;
                });

                // 按钮点击事件
                document.getElementById("send").onclick = function () {
                    var text_area = document.getElementById("output");
                    if (!text_area.value) {
                        return;
                    }
                    // js调用qt中的方法
                    pyjs.receive_str_from_js(text_area.value)
                    text_area.value = "";
                }
            });
}
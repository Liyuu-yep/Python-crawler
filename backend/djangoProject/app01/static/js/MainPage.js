/*点击登录会自动关闭注册弹窗，反之*/
const loginCheckbox = document.getElementById('display');
const registerCheckbox = document.getElementById('display2');

/*loginCheckbox.addEventListener('change', () => {
    if (loginCheckbox.checked) {
        // 登录复选框被选中，显示登录弹窗，同时关闭注册弹窗
        registerCheckbox.checked = false;
    }
});*/

// 对于登录弹出窗口
loginCheckbox.addEventListener('change', () => {
    if (loginCheckbox.checked) {
        // 仅关闭注册弹出窗口
        registerCheckbox.checked = false;
    }
});

/*registerCheckbox.addEventListener('change', () => {
    if (registerCheckbox.checked) {
        // 注册复选框被选中，显示注册弹窗，同时关闭登录弹窗
        loginCheckbox.checked = false;
    }
});*/

registerCheckbox.addEventListener('change', () => {
    if (registerCheckbox.checked) {
        // 仅关闭登录弹出窗口
        loginCheckbox.checked = false;
    }
});

/*点击登录弹窗中的注册会跳转注册弹窗，反之*/
const openRegisterLink = document.querySelector('.container-login .forgot a');
const openLoginLink = document.querySelector('.container-register .forgot a');

openRegisterLink.addEventListener('click', (event) => {
    event.preventDefault();
    loginCheckbox.checked = false;
    registerCheckbox.checked = true;
});

openLoginLink.addEventListener('click', (event) => {
    event.preventDefault();
    registerCheckbox.checked = false;
    loginCheckbox.checked = true;
});
/*个人中心等未登录会打开登录框*/
document.addEventListener('DOMContentLoaded', function() {
    // 获取登录复选框和链接元素
    const loginCheckbox = document.getElementById('display');
    const personalCenterLink = document.querySelector('.word2[href="S-MainPage2.html"]');
    const fanJuInformationLink = document.querySelector('.word2[href="FanJuInformation.html"]');
    const dataAnalysisLink = document.querySelector('.word2[href=""]');
    const overallRankingsLink = document.querySelector('.word2[href="AfterLogin.html"]');

    // 添加事件监听器来在点击链接时显示登录弹窗
    personalCenterLink.addEventListener('click', (event) => {
        event.preventDefault(); // 阻止默认的链接行为
        loginCheckbox.checked = true; // 显示登录弹窗
    });

    fanJuInformationLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginCheckbox.checked = true;
    });

    dataAnalysisLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginCheckbox.checked = true;
    });

    overallRankingsLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginCheckbox.checked = true;
    });
});
/*点击注册后再点击个人中心关闭重复弹窗*/
document.addEventListener('DOMContentLoaded', function() {
    const loginCheckbox = document.getElementById('display');
    const registerCheckbox = document.getElementById('display2');

    const personalCenterLink = document.querySelector('.word2[href="S-MainPage2.html"]');
    const fanJuInformationLink = document.querySelector('.word2[href="FanJuInformation.html"]');
    const dataAnalysisLink = document.querySelector('.word2[href=""]');
    const overallRankingsLink = document.querySelector('.word2[href="AfterLogin.html"]');

    personalCenterLink.addEventListener('click', (event) => {
        event.preventDefault();
        // 显示登录弹窗，同时关闭注册弹窗
        loginCheckbox.checked = true;
        registerCheckbox.checked = false;
    });

    fanJuInformationLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginCheckbox.checked = true;
        registerCheckbox.checked = false;
    });

    dataAnalysisLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginCheckbox.checked = true;
        registerCheckbox.checked = false;
    });

    overallRankingsLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginCheckbox.checked = true;
        registerCheckbox.checked = false;
    });
});

/*清除错误信息*/
const loginForm = document.querySelector('.container-login form');

loginCheckbox.addEventListener('change', () => {
    if (loginCheckbox.checked) {
        // 清除表单字段和错误消息
        loginForm.reset();
        const errorMessages = document.querySelectorAll('.container-login h5');
        errorMessages.forEach(message => message.textContent = '');

        // 仅关闭注册弹出窗口
        registerCheckbox.checked = false;
    }
});
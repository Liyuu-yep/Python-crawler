    const menuItems = document.querySelectorAll('.menu-item');
    const menuContents = document.querySelectorAll('.menu-content');

    menuItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            menuContents.forEach(content => content.style.display = 'none');
            menuContents[index].style.display = 'block';
        });
    });
    /*本地上传头像并预览*/
    const avatarInput = document.getElementById('avatarInput');
    const previewImage = document.getElementById('previewImage');
    avatarInput.addEventListener('change', (event) => {
        const selectedFile = event.target.files[0];

        if (selectedFile) {
            const reader = new FileReader();

            reader.onload = (e) => {
                previewImage.src = e.target.result;
                previewImage.style.display = 'block'; // 显示预览图
            }

            reader.readAsDataURL(selectedFile);
        }
    });
    /*更新右上角头像框*/
    // 假设用户框中的头像元素具有id为"userAvatar"
    const userAvatar = document.getElementById('userAvatar');

    avatarInput.addEventListener('change', (event) => {
        const selectedFile = event.target.files[0];

        if (selectedFile) {
            const reader = new FileReader();

            reader.onload = (e) => {
                previewImage.src = e.target.result;
                previewImage.style.display = 'block';

                // 更新用户框中的头像
                userAvatar.src = e.target.result;
            }

            reader.readAsDataURL(selectedFile);
        }
    });
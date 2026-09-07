const photo =
	    document.getElementById("photo");

const fileName =
	    document.getElementById("file-name");


if (photo) {

	    photo.addEventListener(
		            "change",
		            () => {

				                if (photo.files.length) {

							                fileName.textContent =
								                    photo.files[0].name;

							            } else {

									                    fileName.textContent =
										                        "No file selected";

									                }

				            }
		        );

}


function scrollToUpload() {

	    document
	        .getElementById("upload")
	        ?.scrollIntoView({
			            behavior: "smooth"
			        });

}


let addCategory = document.getElementById('add-category')




if (addCategory!==null){
	console.log(addCategory)
	addCategory.addEventListener('click', function(){
		// get the form tag and input tag with new category name
		let form = document.getElementById('create-article-form')
		
		let categoryName = document.getElementById('category-to-add')

		// create text inputs with category name 
		var input = document.createElement("input");
		input.name="new-category";
		input.value=categoryName.value


		// some styling to input category
		input.classList.add('btn')
		input.classList.add('btn-primary')
		input.classList.add('rounded')
		input.readOnly = true
		input.style.cssText = `border: 0; outline: none; display:inline-block; padding: 0 0; margin-right:5px; width:${categoryName.value.length*12}px;`
		// insert the new category
		let a = document.getElementById('add-category-btn')
		form.insertBefore(input, a)
		console.log(form)

		//adding delete event when input clicked
		input.addEventListener('click', function(){
			input.remove();
		})

		//clear input field for adding category name
		categoryName.value='';
	})
}
	
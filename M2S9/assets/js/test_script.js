// Get the elements
const btnMostrarForm = document.getElementById('btnMostrarForm');
const formTarea = document.getElementById('formTarea');
const submitTarea = document.getElementById('submitTarea');
const tablaTareas = document.getElementById('tabla-tareas');
const cuerpoTabla = document.getElementById('cuerpo-tabla');

// Toggle form visibility
btnMostrarForm.addEventListener('click', () => {
  formTarea.classList.toggle('d-none');
});

// Add new task to table
submitTarea.addEventListener('click', () => {
  const tareaInput = document.getElementById('agregarTarea');
  const tareaValue = tareaInput.value.trim();
  if (tareaValue) {
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
      <td>${tareaValue}</td>
      <td><button class="btn btn-success">Finalizar</button></td>
    `;
    cuerpoTabla.appendChild(newRow);
    tareaInput.value = '';
  }
});

// Mark task as completed
cuerpoTabla.addEventListener('click', (e) => {
  if (e.target.tagName === 'BUTTON' && e.target.classList.contains('btn-success')) {
    const tareaRow = e.target.parentNode.parentNode;
    tareaRow.classList.add('table-success');
  }
});
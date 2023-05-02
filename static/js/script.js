function updateTime() {
  function addLeadingZero(number) {
  if (number < 10) {
    return "0" + number;
  }
  return number;
}

  var now = new Date();
  var months = [
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря"
  ];
  const month = months[now.getMonth()];
  var date = now.getDate();
  var year = now.getFullYear();
  var hours = addLeadingZero(now.getHours());
  var minutes = addLeadingZero(now.getMinutes());
  var seconds = addLeadingZero(now.getSeconds());

  // format date
  var dateString = date + " " + month + " " + year;

  // format time
  var timeString = hours + ":" + minutes + ":" + seconds;

  // display date and time
  document.getElementById("date").innerHTML = dateString;
  document.getElementById("time").innerHTML = timeString;
}

// update time every second
setInterval(updateTime, 1000);

function handleDragStart(event) {
  // определить тип перетаскиваемого элемента
  const taskData = {
    taskId: event.target.id,
    columnId: event.target.closest('.col-wrapper').id
  };

  // передать данные в event.dataTransfer
  event.dataTransfer.setData('text/plain', JSON.stringify(taskData));
    console.log(`Card "${taskData.taskId}" is being dragged from column to column.`);

}

function handleDragOver(event) {
  // отменить стандартное поведение браузера
  event.preventDefault();

  // определить, может ли элемент быть перетащен в этот контейнер
  const isDropAllowed = event.target.classList.contains('task-list');

  if (isDropAllowed) {
    // позволить сброс элемента в контейнере
    event.dataTransfer.dropEffect = 'move';
  } else {
    // запретить сброс элемента в контейнере
    event.dataTransfer.dropEffect = 'none';
  }
}

function updateTaskColumn(taskId, newColumnId) {
  // Найти задачу по ее ID
  const task = document.getElementById(`task-${taskId}`);

  // Обновить свойство column_id задачи на newColumnId
  task.dataset.columnId = newColumnId;

  // Отправить запрос на сервер для сохранения обновленной задачи (если требуется)
  // Например, можно отправить POST-запрос на сервер с данными об обновленной задаче:
  fetch(`/tasks/${taskId}`, {
    method: 'POST',
    body: JSON.stringify({ column_id: newColumnId }),
    headers: {
      'Content-Type': 'application/json'
    }
  }).then(response => {
    if (response.ok) {
      // Обновить задачу на странице (если требуется)
    } else {
      console.error('Ошибка при сохранении задачи');
    }
  }).catch(error => {
    console.error('Ошибка при отправке запроса на сервер', error);
  });
}

function handleDrop(e) {
  e.preventDefault();
  const taskId = e.dataTransfer.getData('taskId');
  const currentColumnId = e.dataTransfer.getData('columnId');
  const newColumnId = e.target.closest('.col-wrapper').dataset.columnId;
  const currentTaskEl = document.querySelector(`#task-${taskId}`);
  const newColumnEl = document.querySelector(`#col-${newColumnId} .task-wrapper`);

  // Не делаем ничего, если задача переносится в тот же столбец
  if (currentColumnId === newColumnId) {
    return;
  }

  // Переносим задачу в новый столбец
  newColumnEl.appendChild(currentTaskEl);

  // Обновляем информацию о столбце, в котором находится задача
  updateTaskColumn(taskId, newColumnId);
}

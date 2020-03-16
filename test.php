<?php
	//Получаем данные из глобальной переменной $_POST, так как мы передаем данные методом POST
	$one_value_question = $_POST['one_value']; // Вытаскиваем ответ на первый вопрос в переменную
	
	/* Вопрос второй с несколькими вариантами ответов */
	$value_one = $_POST['value_one']; 
	$value_two = $_POST['value_two']; 
	$value_three = $_POST['value_three']; 
	$value_four = $_POST['value_four']; 
	$value_five = $_POST['value_five']; 
	
	$result = 0; // результат будет в процентах правильных ответов
	
	/* проверяем первый вопрос */
	if ($one_value_question == "c") {
		$result += 50;
	} else {
        $result +=0;
    }
	
	/* Проверяем второй вопрос */
	$subresult = 0; // дополнительная переменная для подсчёта правильности ответов на 2 вопрос
	
		/* если выбран вариант с подозрением на вирус, то счётчик++ */
	if ($value_one != '') {
		$subresult++;
	}
	if ($value_three != '') {
		$subresult++;
	}
		/* если выбран вариант с профилактикой, то счётчик-- */
	if ($value_two != '') {
		$subresult--;
	}
	if ($value_four != '') {
		$subresult--;
	}

        /* если выбран нейтральный вариант, то счётчик +=0 */
	if ($value_five != '') {
		$subresult += 0;
	}
	

        /* здесь проводится расчёт по второму вопросу */
	if ($subresult == 2) {
		$result += 50;
	} else if ($subresult == 1) {
        $result += 25;
    } else if ($subresult == -1) {
        $result -= 5;
    } else if ($subresult == -2) {
        $result -= 10;
    } else  {
        $result += 0;
    }

    if ($result <= 0) {
        $result = 1;
    }
    
    if ($result >= 100) {
        $result = 99;
    }
	
	echo "<center>Вероятность заболеть <strong>$result%</strong></center>";
    
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width = device-width, initial-scale = 1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title> Keat </title>
    <style>
        .button_link {
            position: relative;
            padding: 1%;
            border: 1px solid black;
            border-radius: 3px;
            text-decoration: none;
        }
    </style>
</head>

<body>
    <br>
    <br>
    <center><a class="button_link" href="index.html">Вернуться к тесту</a></center>
</body>

</html>

const add = function() {
    let sum = 0;
  
    return function() {
      sum++;
      console.log(`${sum}`);
    }
  }

  
const total = add();



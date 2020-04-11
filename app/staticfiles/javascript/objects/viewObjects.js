class DayOfWeekView extends React.Component {
    preventDefault(event) {
      event.preventDefault();
    }
    componentDidMount (event){
      //remove filler text if needed
      if (this.props.recipes.length!=0){
        document.getElementById(this.props.dayId).innerHTML='';
      }
      //move recipes to the right days
      for (var i = 0; i < this.props.recipes.length; i++) {
        var targetRecipe = this.props.recipes[i];
        var targetDay = this.props.dayId;
        var dayElem=document.getElementById(targetDay);
        dayElem.appendChild(document.getElementById(targetRecipe));
        //disable dragging for recipe
        document.getElementById(targetRecipe).draggable=false;
        document.getElementById(targetRecipe).ondragstart=false;
        document.getElementById(targetRecipe).touchstart=false;
      }
    }
    onDragLeave_handler(event){
      event.preventDefault();
      if (event.target.classList.contains("dayDrop")){
        event.target.classList.remove('day_drag_hover');
      } else {
        event.target.parentElement.classList.remove('day_drag_hover');
      }
    }
    render() {
        return (
          <div className="panel panel-default">
            <div className="panel-heading">{this.props.dayName}</div>
            <div id={this.props.dayId} className="dayDrop emptyDay panel-body" >
              <div className="dayPlaceholder">No meals planned</div>
            </div>
          </div>

        );
    }
}

class WeekView extends React.Component {
    render() {
        var days = this.props.days;
        var recipeGuidsByDay = this.props.recipeGuidsByDay;
        return (
          <div>
            {Object.keys(days).map((id, vals) => (
              <DayOfWeekView key={id} dayId={days[id]['id']} dayName={days[id]["dayName"]} recipes={recipeGuidsByDay[id]["recipeGuids"]}/>
            ))}
          </div>
        );
    }
}

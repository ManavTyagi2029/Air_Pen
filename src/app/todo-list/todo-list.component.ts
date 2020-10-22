import { Component, OnInit } from '@angular/core';
import { TodoEntry } from '../todo-entry';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  title = 'todo';

  newtitle = '';
  newdate  = '';
  newdesc  = '';

  todo_list : TodoEntry[] = [];

  public add_todo(): void {
    this.todo_list.push(new TodoEntry(this.newtitle, this.newdate, this.newdesc));
  }

  public delete_todo(i: number): void {
    this.todo_list.splice(i, 1);
  }
}

import http from '../http-common';

class EmployeeDataService {
  registerUser(email: string, password: string, first_name: string, last_name: string) {
    return 
  }
  
  getAll() {
    return http.get('api/v1/employee');
  }

  getDirectReports() {
    return http.get('api/v1/employee?direct-reports=True');
  }

  getEmployeeNextPerformanceReview(pk: number) {
    return http.get(`api/v1/employee/${pk}/employee_next_performance_review`)
  }
}

export default new EmployeeDataService();

% rebase('base.tpl', title='Records', page='db')
<div id="records">
    <div class="table-responsive">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Date</th>
                    <th>Time</th>
                    <th>Temperature</th>
                    <th>Humidity</th>
                    <th>Air pressure</th>
                    <th>RGBW value</th>
                </tr>
            </thead>
            <tbody>
            % from datetime import datetime
            % for item in records:
                <tr>
                    <th scope="row">{{item[0]}}</th>
                    <%
                    date_time = datetime.fromtimestamp(item[8]/1000.0)
                    date = date_time.strftime('%b %e %Y')
                    time = date_time.strftime('%H:%M:%S')
                    %>
                    <td>{{date}}</td>
                    <td>{{time}}</td>
                    <td>{{item[1]}} °C</td>
                    <td>{{item[2]}} %</td>
                    <td>{{item[3]}} hpa</td>
                    % rgbw =  "({}, {}, {}, {})".format(item[4], item[5], item[6], item[7])
                    <td>{{rgbw}}</td>
                </tr>
            % end
            </tbody>
        </table>
    </div>
</div>
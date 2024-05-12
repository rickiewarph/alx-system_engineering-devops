POSTMORTEN OF THE GC APP.

Issue Summary:

Duration.
The outage occurred from 10:00 AM to 11:00 AM on May 1st, 2024 (UTC+3).

Impact.
The outage affected the Nairobi city garbage collection app, resulting in service unavailability and slow response times. Approximately 30% of users experienced disruptions during this period.

Root Cause.
The outage was primarily caused by communication failures due to interference or signal loss in the wireless communication modules.

Timeline.

10:00 AM: The issue was detected through monitoring alerts indicating a spike in error rates and latency.
10:10 AM: The devs began investigating the issue, focusing on potential backend service failures and network connectivity issues.
10:30 AM: Initial assumption suggested a possible backend service outage or database connection problem.
10:35 AM: Further investigation revealed no issues with backend services or database connectivity, leading to consideration of external factors such as communication failures.
10:45 AM: Escalation to the network engineering team to analyze wireless communication modules and identify potential interference sources.
10:55 AM: The incident was resolved after implementing corrective measures to mitigate interference and improve signal stability in the communication modules.

Root Cause and Resolution.

Root Cause.
The primary cause of the outage was communication failures resulting from interference or signal loss in the wireless communication modules used by the garbage collection app.

Resolution.
The issue was resolved by implementing corrective measures to address interference sources, optimize signal transmission, and improve the overall stability of the communication modules.

Corrective and Preventative Measures

Improvements/Fixes.

Enhance signal processing algorithms to mitigate interference and improve signal reliability.
Implement redundancy and failover mechanisms to ensure service continuity in the event of communication failures.
Conduct regular performance testing and optimization to address scalability challenges and ensure the system can handle increased data volume and user traffic.

Tasks to Address the Issue.

Conduct a comprehensive review of wireless communication infrastructure to identify and eliminate interference sources.
Update communication module firmware and software to the latest versions to benefit from performance improvements and bug fixes.
Implement automated monitoring and alerting systems to proactively detect and respond to communication issues in real-time.
Collaborate with network providers to optimize signal strength and ensure consistent connectivity in all operational areas.
By implementing these measures, we aim to minimize the likelihood of future outages and enhance the overall reliability and performance of the Nairobi city garbage collection app.

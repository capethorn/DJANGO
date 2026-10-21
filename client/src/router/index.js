import { createRouter, createWebHistory } from 'vue-router'

import SubscriptionView from '../components/SubscriptionView.vue'
import OptionView from '../components/OptionView.vue'
import OptionToSubscriptionView from '../components/OptionToSubscriptionView.vue'
import AppointmentCoachView from '../components/AppointmentCoachView.vue'
import AppointmentGroupView from '../components/AppointmentGroupView.vue'
import AdditionallyView from '../components/AdditionallyView.vue'
import AddresView from '../components/AddresView.vue'
import AppointmentToGroupView from '../components/AppointmentToGroupView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/subscription', component: SubscriptionView },
    { path: '/option', component: OptionView },
    { path: '/option-to-subscription', component: OptionToSubscriptionView },
    { path: '/appointment-coach', component: AppointmentCoachView },
    { path: '/appointment-group', component: AppointmentGroupView },
    { path: '/additionally', component: AdditionallyView },
    { path: '/addres', component: AddresView },
    { path: '/appointment-to-group', component: AppointmentToGroupView },
  ]
})

export default router
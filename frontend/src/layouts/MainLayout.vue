<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>

        <q-toolbar-title>
          Hi {{ name() }}
        </q-toolbar-title>

        <div>
          <q-item
            clickable
            @click='logout'
          >
            <q-item-section>
              <q-item-label>Log Out</q-item-label>
            </q-item-section>
          </q-item>
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import NavLink from 'components/NavLink.vue'

import { Component, Vue } from 'vue-property-decorator'

interface LinkData {
  title: string;
  icon: string;
  link: string;
  managerOnly?: boolean;
}

const linksData: Array<LinkData> = [
  {
    title: 'Dashboard',
    icon: 'dashboard',
    link: '/dashboard'
  },
  {
    title: 'Performance Reviews',
    icon: 'assignment_turned_in',
    link: '/reviews',
    managerOnly: true
  },
  {
    title: 'Time off Requests',
    icon: 'schedule',
    link: '/timeoff'
  },
];

interface LayoutData {
  name: string
}

@Component({
  components: { NavLink }
})
export default class MainLayout extends Vue{
  private leftDrawerOpen = false;
  private navLinks: Array<LinkData> = linksData;
  private name() {
    return this.$store.getters['userModule/getEmployeeProfile'].name // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  public getCurrentUser(): void {
    if (!this.$store.getters['userModule/isProfileLoaded']) { // eslint-disable-line @typescript-eslint/no-unsafe-member-access
      this.$store.dispatch('userModule/userRequest')
        .catch(e => {
          console.error('Error getting user from store:', e)
        })
    }
  }
  public getImages(): void {
    this.$store.dispatch('memoriesModule/getImages')
      .catch(e => {
        console.error('Error getting images from store:', e)
      })
  }
  public getStories(): void {
    this.$store.dispatch('memoriesModule/getStories')
      .catch(e => {
        console.error('Error getting stories from store:', e)
      })
  }
  public getVideos(): void {
    this.$store.dispatch('memoriesModule/getVideos')
      .catch(e => {
        console.error('Error getting videos from store:', e)
      })
  }
  public getAudio(): void {
    this.$store.dispatch('memoriesModule/getAudio')
      .catch(e => {
        console.error('Error getting audio from store:', e)
      })
  }
  public logout(): void {
    this.$store.dispatch('authModule/authLogout')
    .then(() => {
      this.$router.push('/auth/login')
        .catch(e => {
          console.error('Error navigating to login page after logout', e)
        })
    })
    .catch(e => {
      console.error('Error logging out', e);
    })
  }
  mounted() {
    this.getCurrentUser();
    this.getImages();
    this.getStories();
    this.getVideos();
    this.getAudio();
  }
};
</script>

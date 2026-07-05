---
type: Jurisdiction
title: "De Soto Parish, LA"
classification: county
fips: "22031"
state: "LA"
demographics:
  population: 27026
  population_under_18: 6459
  population_18_64: 15492
  population_65_plus: 5075
  median_household_income: 48578
  poverty_rate: 21.53
  homeownership_rate: 77.15
  unemployment_rate: 5.98
  median_home_value: 154900
  gini_index: 0.489
  vacancy_rate: 17.27
  race_white: 16065
  race_black: 9388
  race_asian: 94
  race_native: 125
  hispanic: 863
  bachelors_plus: 3836
districts:
  - to: "us/states/la/districts/06"
    rel: in-district
    area_weight: 0.5959
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.4036
  - to: "us/states/la/districts/senate/38"
    rel: in-district
    area_weight: 0.5284
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 0.4711
  - to: "us/states/la/districts/house/7"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# De Soto Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27026 |
| Under 18 | 6459 |
| 18–64 | 15492 |
| 65+ | 5075 |
| Median household income | 48578 |
| Poverty rate | 21.53 |
| Homeownership rate | 77.15 |
| Unemployment rate | 5.98 |
| Median home value | 154900 |
| Gini index | 0.489 |
| Vacancy rate | 17.27 |
| White | 16065 |
| Black | 9388 |
| Asian | 94 |
| Native | 125 |
| Hispanic/Latino | 863 |
| Bachelor's or higher | 3836 |

## Districts

- [LA-06](/us/states/la/districts/06.md) — 60% (congressional)
- [LA-04](/us/states/la/districts/04.md) — 40% (congressional)
- [LA Senate District 38](/us/states/la/districts/senate/38.md) — 53% (state senate)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 47% (state senate)
- [LA House District 7](/us/states/la/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

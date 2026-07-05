---
type: Jurisdiction
title: "Bossier Parish, LA"
classification: county
fips: "22015"
state: "LA"
demographics:
  population: 129789
  population_under_18: 32213
  population_18_64: 77559
  population_65_plus: 20017
  median_household_income: 69617
  poverty_rate: 15.92
  homeownership_rate: 65.09
  unemployment_rate: 5.92
  median_home_value: 227200
  gini_index: 0.4621
  vacancy_rate: 10.43
  race_white: 82341
  race_black: 30836
  race_asian: 2105
  race_native: 517
  hispanic: 10784
  bachelors_plus: 34435
districts:
  - to: "us/states/la/districts/04"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/la/districts/senate/36"
    rel: in-district
    area_weight: 0.9606
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 0.0355
  - to: "us/states/la/districts/house/10"
    rel: in-district
    area_weight: 0.5032
  - to: "us/states/la/districts/house/9"
    rel: in-district
    area_weight: 0.2324
  - to: "us/states/la/districts/house/5"
    rel: in-district
    area_weight: 0.171
  - to: "us/states/la/districts/house/8"
    rel: in-district
    area_weight: 0.0846
  - to: "us/states/la/districts/house/2"
    rel: in-district
    area_weight: 0.0084
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Bossier Parish, LA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 129789 |
| Under 18 | 32213 |
| 18–64 | 77559 |
| 65+ | 20017 |
| Median household income | 69617 |
| Poverty rate | 15.92 |
| Homeownership rate | 65.09 |
| Unemployment rate | 5.92 |
| Median home value | 227200 |
| Gini index | 0.4621 |
| Vacancy rate | 10.43 |
| White | 82341 |
| Black | 30836 |
| Asian | 2105 |
| Native | 517 |
| Hispanic/Latino | 10784 |
| Bachelor's or higher | 34435 |

## Districts

- [LA-04](/us/states/la/districts/04.md) — 100% (congressional)
- [LA Senate District 36](/us/states/la/districts/senate/36.md) — 96% (state senate)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 4% (state senate)
- [LA House District 10](/us/states/la/districts/house/10.md) — 50% (state house)
- [LA House District 9](/us/states/la/districts/house/9.md) — 23% (state house)
- [LA House District 5](/us/states/la/districts/house/5.md) — 17% (state house)
- [LA House District 8](/us/states/la/districts/house/8.md) — 8% (state house)
- [LA House District 2](/us/states/la/districts/house/2.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

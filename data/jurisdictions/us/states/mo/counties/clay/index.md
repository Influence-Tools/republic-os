---
type: Jurisdiction
title: "Clay County, MO"
classification: county
fips: "29047"
state: "MO"
demographics:
  population: 258122
  population_under_18: 60745
  population_18_64: 157947
  population_65_plus: 39430
  median_household_income: 88468
  poverty_rate: 8.47
  homeownership_rate: 69.49
  unemployment_rate: 3.77
  median_home_value: 275600
  gini_index: 0.4181
  vacancy_rate: 5.15
  race_white: 204377
  race_black: 18039
  race_asian: 6676
  race_native: 1046
  hispanic: 20621
  bachelors_plus: 87485
districts:
  - to: "us/states/mo/districts/06"
    rel: in-district
    area_weight: 0.8058
  - to: "us/states/mo/districts/05"
    rel: in-district
    area_weight: 0.1941
  - to: "us/states/mo/districts/senate/21"
    rel: in-district
    area_weight: 0.7193
  - to: "us/states/mo/districts/senate/17"
    rel: in-district
    area_weight: 0.2805
  - to: "us/states/mo/districts/house/8"
    rel: in-district
    area_weight: 0.3918
  - to: "us/states/mo/districts/house/39"
    rel: in-district
    area_weight: 0.3062
  - to: "us/states/mo/districts/house/17"
    rel: in-district
    area_weight: 0.0955
  - to: "us/states/mo/districts/house/38"
    rel: in-district
    area_weight: 0.0811
  - to: "us/states/mo/districts/house/16"
    rel: in-district
    area_weight: 0.051
  - to: "us/states/mo/districts/house/18"
    rel: in-district
    area_weight: 0.0457
  - to: "us/states/mo/districts/house/15"
    rel: in-district
    area_weight: 0.0287
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Clay County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 258122 |
| Under 18 | 60745 |
| 18–64 | 157947 |
| 65+ | 39430 |
| Median household income | 88468 |
| Poverty rate | 8.47 |
| Homeownership rate | 69.49 |
| Unemployment rate | 3.77 |
| Median home value | 275600 |
| Gini index | 0.4181 |
| Vacancy rate | 5.15 |
| White | 204377 |
| Black | 18039 |
| Asian | 6676 |
| Native | 1046 |
| Hispanic/Latino | 20621 |
| Bachelor's or higher | 87485 |

## Districts

- [MO-06](/us/states/mo/districts/06.md) — 81% (congressional)
- [MO-05](/us/states/mo/districts/05.md) — 19% (congressional)
- [MO Senate District 21](/us/states/mo/districts/senate/21.md) — 72% (state senate)
- [MO Senate District 17](/us/states/mo/districts/senate/17.md) — 28% (state senate)
- [MO House District 8](/us/states/mo/districts/house/8.md) — 39% (state house)
- [MO House District 39](/us/states/mo/districts/house/39.md) — 31% (state house)
- [MO House District 17](/us/states/mo/districts/house/17.md) — 10% (state house)
- [MO House District 38](/us/states/mo/districts/house/38.md) — 8% (state house)
- [MO House District 16](/us/states/mo/districts/house/16.md) — 5% (state house)
- [MO House District 18](/us/states/mo/districts/house/18.md) — 5% (state house)
- [MO House District 15](/us/states/mo/districts/house/15.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

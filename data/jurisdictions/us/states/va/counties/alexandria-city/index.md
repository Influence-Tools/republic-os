---
type: Jurisdiction
title: "Alexandria city, VA"
classification: county
fips: "51510"
state: "VA"
demographics:
  population: 159102
  population_under_18: 29067
  population_18_64: 71441
  population_65_plus: 58594
  median_household_income: 124593
  poverty_rate: 5.94
  homeownership_rate: 43.18
  unemployment_rate: 2.08
  median_home_value: 704200
  gini_index: 0.4401
  vacancy_rate: 3.25
  race_white: 80547
  race_black: 33966
  race_asian: 11628
  race_native: 1887
  hispanic: 29519
  bachelors_plus: 130281
districts:
  - to: "us/states/va/districts/08"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/va/districts/senate/39"
    rel: in-district
    area_weight: 0.9979
  - to: "us/states/va/districts/house/5"
    rel: in-district
    area_weight: 0.5804
  - to: "us/states/va/districts/house/4"
    rel: in-district
    area_weight: 0.2243
  - to: "us/states/va/districts/house/3"
    rel: in-district
    area_weight: 0.1932
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Alexandria city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 159102 |
| Under 18 | 29067 |
| 18–64 | 71441 |
| 65+ | 58594 |
| Median household income | 124593 |
| Poverty rate | 5.94 |
| Homeownership rate | 43.18 |
| Unemployment rate | 2.08 |
| Median home value | 704200 |
| Gini index | 0.4401 |
| Vacancy rate | 3.25 |
| White | 80547 |
| Black | 33966 |
| Asian | 11628 |
| Native | 1887 |
| Hispanic/Latino | 29519 |
| Bachelor's or higher | 130281 |

## Districts

- [VA-08](/us/states/va/districts/08.md) — 100% (congressional)
- [VA Senate District 39](/us/states/va/districts/senate/39.md) — 100% (state senate)
- [VA House District 5](/us/states/va/districts/house/5.md) — 58% (state house)
- [VA House District 4](/us/states/va/districts/house/4.md) — 22% (state house)
- [VA House District 3](/us/states/va/districts/house/3.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

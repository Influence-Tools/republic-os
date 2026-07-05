---
type: Jurisdiction
title: "Suffolk city, VA"
classification: county
fips: "51800"
state: "VA"
demographics:
  population: 98796
  population_under_18: 25429
  population_18_64: 32820
  population_65_plus: 40547
  median_household_income: 92666
  poverty_rate: 9.39
  homeownership_rate: 70.74
  unemployment_rate: 4.96
  median_home_value: 347400
  gini_index: 0.4339
  vacancy_rate: 6.4
  race_white: 45942
  race_black: 41515
  race_asian: 1843
  race_native: 573
  hispanic: 5172
  bachelors_plus: 31430
districts:
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.9723
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 0.9698
  - to: "us/states/va/districts/house/89"
    rel: in-district
    area_weight: 0.7115
  - to: "us/states/va/districts/house/84"
    rel: in-district
    area_weight: 0.2583
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Suffolk city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 98796 |
| Under 18 | 25429 |
| 18–64 | 32820 |
| 65+ | 40547 |
| Median household income | 92666 |
| Poverty rate | 9.39 |
| Homeownership rate | 70.74 |
| Unemployment rate | 4.96 |
| Median home value | 347400 |
| Gini index | 0.4339 |
| Vacancy rate | 6.4 |
| White | 45942 |
| Black | 41515 |
| Asian | 1843 |
| Native | 573 |
| Hispanic/Latino | 5172 |
| Bachelor's or higher | 31430 |

## Districts

- [VA-02](/us/states/va/districts/02.md) — 97% (congressional)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 97% (state senate)
- [VA House District 89](/us/states/va/districts/house/89.md) — 71% (state house)
- [VA House District 84](/us/states/va/districts/house/84.md) — 26% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

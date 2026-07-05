---
type: Jurisdiction
title: "Richmond city, VA"
classification: county
fips: "51760"
state: "VA"
demographics:
  population: 229359
  population_under_18: 48334
  population_18_64: 99634
  population_65_plus: 81391
  median_household_income: 64587
  poverty_rate: 18.2
  homeownership_rate: 43.53
  unemployment_rate: 5.73
  median_home_value: 353000
  gini_index: 0.5132
  vacancy_rate: 8.72
  race_white: 98088
  race_black: 93993
  race_asian: 4857
  race_native: 569
  hispanic: 24539
  bachelors_plus: 105217
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.9914
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.0086
  - to: "us/states/va/districts/senate/14"
    rel: in-district
    area_weight: 0.7133
  - to: "us/states/va/districts/senate/15"
    rel: in-district
    area_weight: 0.2857
  - to: "us/states/va/districts/house/78"
    rel: in-district
    area_weight: 0.3971
  - to: "us/states/va/districts/house/79"
    rel: in-district
    area_weight: 0.3694
  - to: "us/states/va/districts/house/77"
    rel: in-district
    area_weight: 0.232
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Richmond city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 229359 |
| Under 18 | 48334 |
| 18–64 | 99634 |
| 65+ | 81391 |
| Median household income | 64587 |
| Poverty rate | 18.2 |
| Homeownership rate | 43.53 |
| Unemployment rate | 5.73 |
| Median home value | 353000 |
| Gini index | 0.5132 |
| Vacancy rate | 8.72 |
| White | 98088 |
| Black | 93993 |
| Asian | 4857 |
| Native | 569 |
| Hispanic/Latino | 24539 |
| Bachelor's or higher | 105217 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 99% (congressional)
- [VA-01](/us/states/va/districts/01.md) — 1% (congressional)
- [VA Senate District 14](/us/states/va/districts/senate/14.md) — 71% (state senate)
- [VA Senate District 15](/us/states/va/districts/senate/15.md) — 29% (state senate)
- [VA House District 78](/us/states/va/districts/house/78.md) — 40% (state house)
- [VA House District 79](/us/states/va/districts/house/79.md) — 37% (state house)
- [VA House District 77](/us/states/va/districts/house/77.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

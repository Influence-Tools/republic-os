---
type: Jurisdiction
title: "Anderson County, KY"
classification: county
fips: "21005"
state: "KY"
demographics:
  population: 24353
  population_under_18: 5634
  population_18_64: 14587
  population_65_plus: 4132
  median_household_income: 74488
  poverty_rate: 11.47
  homeownership_rate: 77.61
  unemployment_rate: 2.23
  median_home_value: 225100
  gini_index: 0.3973
  vacancy_rate: 6.52
  race_white: 22529
  race_black: 523
  race_asian: 82
  race_native: 0
  hispanic: 639
  bachelors_plus: 5942
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.5147
  - to: "us/states/ky/districts/01"
    rel: in-district
    area_weight: 0.4831
  - to: "us/states/ky/districts/senate/7"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ky/districts/house/53"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Anderson County, KY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24353 |
| Under 18 | 5634 |
| 18–64 | 14587 |
| 65+ | 4132 |
| Median household income | 74488 |
| Poverty rate | 11.47 |
| Homeownership rate | 77.61 |
| Unemployment rate | 2.23 |
| Median home value | 225100 |
| Gini index | 0.3973 |
| Vacancy rate | 6.52 |
| White | 22529 |
| Black | 523 |
| Asian | 82 |
| Native | 0 |
| Hispanic/Latino | 639 |
| Bachelor's or higher | 5942 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 51% (congressional)
- [KY-01](/us/states/ky/districts/01.md) — 48% (congressional)
- [KY Senate District 7](/us/states/ky/districts/senate/7.md) — 100% (state senate)
- [KY House District 53](/us/states/ky/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

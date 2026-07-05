---
type: Jurisdiction
title: "Greene County, AR"
classification: county
fips: "05055"
state: "AR"
demographics:
  population: 46432
  population_under_18: 11123
  population_18_64: 27776
  population_65_plus: 7533
  median_household_income: 57839
  poverty_rate: 17.41
  homeownership_rate: 66.19
  unemployment_rate: 5.88
  median_home_value: 169300
  gini_index: 0.4314
  vacancy_rate: 8.21
  race_white: 41506
  race_black: 1059
  race_asian: 191
  race_native: 19
  hispanic: 1741
  bachelors_plus: 7266
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ar/districts/senate/21"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/ar/districts/house/1"
    rel: in-district
    area_weight: 0.6905
  - to: "us/states/ar/districts/house/30"
    rel: in-district
    area_weight: 0.2086
  - to: "us/states/ar/districts/house/31"
    rel: in-district
    area_weight: 0.1005
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Greene County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 46432 |
| Under 18 | 11123 |
| 18–64 | 27776 |
| 65+ | 7533 |
| Median household income | 57839 |
| Poverty rate | 17.41 |
| Homeownership rate | 66.19 |
| Unemployment rate | 5.88 |
| Median home value | 169300 |
| Gini index | 0.4314 |
| Vacancy rate | 8.21 |
| White | 41506 |
| Black | 1059 |
| Asian | 191 |
| Native | 19 |
| Hispanic/Latino | 1741 |
| Bachelor's or higher | 7266 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 21](/us/states/ar/districts/senate/21.md) — 100% (state senate)
- [AR House District 1](/us/states/ar/districts/house/1.md) — 69% (state house)
- [AR House District 30](/us/states/ar/districts/house/30.md) — 21% (state house)
- [AR House District 31](/us/states/ar/districts/house/31.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

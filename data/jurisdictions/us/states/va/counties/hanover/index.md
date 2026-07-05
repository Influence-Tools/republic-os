---
type: Jurisdiction
title: "Hanover County, VA"
classification: county
fips: "51085"
state: "VA"
demographics:
  population: 112879
  population_under_18: 24361
  population_18_64: 66846
  population_65_plus: 21672
  median_household_income: 112805
  poverty_rate: 5.69
  homeownership_rate: 82.12
  unemployment_rate: 2.72
  median_home_value: 400400
  gini_index: 0.4246
  vacancy_rate: 4.26
  race_white: 91982
  race_black: 9497
  race_asian: 2414
  race_native: 167
  hispanic: 4474
  bachelors_plus: 46492
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.5137
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.4788
  - to: "us/states/va/districts/07"
    rel: in-district
    area_weight: 0.0065
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.6687
  - to: "us/states/va/districts/senate/26"
    rel: in-district
    area_weight: 0.3306
  - to: "us/states/va/districts/house/59"
    rel: in-district
    area_weight: 0.6197
  - to: "us/states/va/districts/house/60"
    rel: in-district
    area_weight: 0.3797
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Hanover County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 112879 |
| Under 18 | 24361 |
| 18–64 | 66846 |
| 65+ | 21672 |
| Median household income | 112805 |
| Poverty rate | 5.69 |
| Homeownership rate | 82.12 |
| Unemployment rate | 2.72 |
| Median home value | 400400 |
| Gini index | 0.4246 |
| Vacancy rate | 4.26 |
| White | 91982 |
| Black | 9497 |
| Asian | 2414 |
| Native | 167 |
| Hispanic/Latino | 4474 |
| Bachelor's or higher | 46492 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 51% (congressional)
- [VA-05](/us/states/va/districts/05.md) — 48% (congressional)
- [VA-07](/us/states/va/districts/07.md) — 1% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 67% (state senate)
- [VA Senate District 26](/us/states/va/districts/senate/26.md) — 33% (state senate)
- [VA House District 59](/us/states/va/districts/house/59.md) — 62% (state house)
- [VA House District 60](/us/states/va/districts/house/60.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

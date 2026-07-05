---
type: Jurisdiction
title: "DeKalb County, AL"
classification: county
fips: "01049"
state: "AL"
demographics:
  population: 72269
  population_under_18: 17353
  population_18_64: 42168
  population_65_plus: 12748
  median_household_income: 51204
  poverty_rate: 22.36
  homeownership_rate: 78.26
  unemployment_rate: 4.14
  median_home_value: 152700
  gini_index: 0.4587
  vacancy_rate: 15.44
  race_white: 57561
  race_black: 975
  race_asian: 142
  race_native: 1215
  hispanic: 12382
  bachelors_plus: 9411
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/al/districts/senate/8"
    rel: in-district
    area_weight: 0.6648
  - to: "us/states/al/districts/senate/10"
    rel: in-district
    area_weight: 0.3352
  - to: "us/states/al/districts/house/24"
    rel: in-district
    area_weight: 0.6529
  - to: "us/states/al/districts/house/39"
    rel: in-district
    area_weight: 0.3469
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# DeKalb County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 72269 |
| Under 18 | 17353 |
| 18–64 | 42168 |
| 65+ | 12748 |
| Median household income | 51204 |
| Poverty rate | 22.36 |
| Homeownership rate | 78.26 |
| Unemployment rate | 4.14 |
| Median home value | 152700 |
| Gini index | 0.4587 |
| Vacancy rate | 15.44 |
| White | 57561 |
| Black | 975 |
| Asian | 142 |
| Native | 1215 |
| Hispanic/Latino | 12382 |
| Bachelor's or higher | 9411 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 8](/us/states/al/districts/senate/8.md) — 66% (state senate)
- [AL Senate District 10](/us/states/al/districts/senate/10.md) — 34% (state senate)
- [AL House District 24](/us/states/al/districts/house/24.md) — 65% (state house)
- [AL House District 39](/us/states/al/districts/house/39.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

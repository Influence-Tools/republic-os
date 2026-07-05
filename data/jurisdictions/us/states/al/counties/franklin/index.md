---
type: Jurisdiction
title: "Franklin County, AL"
classification: county
fips: "01059"
state: "AL"
demographics:
  population: 31966
  population_under_18: 8052
  population_18_64: 18586
  population_65_plus: 5328
  median_household_income: 53338
  poverty_rate: 19.14
  homeownership_rate: 72.37
  unemployment_rate: 3.63
  median_home_value: 136000
  gini_index: 0.4382
  vacancy_rate: 14.63
  race_white: 23800
  race_black: 1296
  race_asian: 22
  race_native: 235
  hispanic: 6573
  bachelors_plus: 4614
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/senate/6"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/al/districts/house/18"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Franklin County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 31966 |
| Under 18 | 8052 |
| 18–64 | 18586 |
| 65+ | 5328 |
| Median household income | 53338 |
| Poverty rate | 19.14 |
| Homeownership rate | 72.37 |
| Unemployment rate | 3.63 |
| Median home value | 136000 |
| Gini index | 0.4382 |
| Vacancy rate | 14.63 |
| White | 23800 |
| Black | 1296 |
| Asian | 22 |
| Native | 235 |
| Hispanic/Latino | 6573 |
| Bachelor's or higher | 4614 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 100% (congressional)
- [AL Senate District 6](/us/states/al/districts/senate/6.md) — 100% (state senate)
- [AL House District 18](/us/states/al/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

---
type: Jurisdiction
title: "San Francisco County, CA"
classification: county
fips: "06075"
state: "CA"
demographics:
  population: 830235
  population_under_18: 113508
  population_18_64: 570217
  population_65_plus: 146510
  median_household_income: 140970
  poverty_rate: 11.15
  homeownership_rate: 38.21
  unemployment_rate: 6.09
  median_home_value: 1394500
  gini_index: 0.5219
  vacancy_rate: 12.21
  race_white: 324342
  race_black: 41333
  race_asian: 292167
  race_native: 6059
  hispanic: 134659
  bachelors_plus: 567198
districts:
  - to: "us/states/ca/districts/11"
    rel: in-district
    area_weight: 0.1853
  - to: "us/states/ca/districts/15"
    rel: in-district
    area_weight: 0.0228
  - to: "us/states/ca/districts/senate/11"
    rel: in-district
    area_weight: 0.2037
  - to: "us/states/ca/districts/house/17"
    rel: in-district
    area_weight: 0.1046
  - to: "us/states/ca/districts/house/19"
    rel: in-district
    area_weight: 0.0991
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# San Francisco County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 830235 |
| Under 18 | 113508 |
| 18–64 | 570217 |
| 65+ | 146510 |
| Median household income | 140970 |
| Poverty rate | 11.15 |
| Homeownership rate | 38.21 |
| Unemployment rate | 6.09 |
| Median home value | 1394500 |
| Gini index | 0.5219 |
| Vacancy rate | 12.21 |
| White | 324342 |
| Black | 41333 |
| Asian | 292167 |
| Native | 6059 |
| Hispanic/Latino | 134659 |
| Bachelor's or higher | 567198 |

## Districts

- [CA-11](/us/states/ca/districts/11.md) — 19% (congressional)
- [CA-15](/us/states/ca/districts/15.md) — 2% (congressional)
- [CA Senate District 11](/us/states/ca/districts/senate/11.md) — 20% (state senate)
- [CA House District 17](/us/states/ca/districts/house/17.md) — 10% (state house)
- [CA House District 19](/us/states/ca/districts/house/19.md) — 10% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

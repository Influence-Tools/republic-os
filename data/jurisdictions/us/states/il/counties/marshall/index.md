---
type: Jurisdiction
title: "Marshall County, IL"
classification: county
fips: "17123"
state: "IL"
demographics:
  population: 11647
  population_under_18: 2378
  population_18_64: 6469
  population_65_plus: 2800
  median_household_income: 71585
  poverty_rate: 11.43
  homeownership_rate: 79.23
  unemployment_rate: 3.82
  median_home_value: 142800
  gini_index: 0.4106
  vacancy_rate: 12.4
  race_white: 10812
  race_black: 47
  race_asian: 10
  race_native: 13
  hispanic: 409
  bachelors_plus: 1994
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.8193
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.1807
  - to: "us/states/il/districts/house/105"
    rel: in-district
    area_weight: 0.8193
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.1807
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Marshall County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11647 |
| Under 18 | 2378 |
| 18–64 | 6469 |
| 65+ | 2800 |
| Median household income | 71585 |
| Poverty rate | 11.43 |
| Homeownership rate | 79.23 |
| Unemployment rate | 3.82 |
| Median home value | 142800 |
| Gini index | 0.4106 |
| Vacancy rate | 12.4 |
| White | 10812 |
| Black | 47 |
| Asian | 10 |
| Native | 13 |
| Hispanic/Latino | 409 |
| Bachelor's or higher | 1994 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 100% (congressional)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 82% (state senate)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 18% (state senate)
- [IL House District 105](/us/states/il/districts/house/105.md) — 82% (state house)
- [IL House District 73](/us/states/il/districts/house/73.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

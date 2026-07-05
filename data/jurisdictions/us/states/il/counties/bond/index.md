---
type: Jurisdiction
title: "Bond County, IL"
classification: county
fips: "17005"
state: "IL"
demographics:
  population: 16716
  population_under_18: 2963
  population_18_64: 10616
  population_65_plus: 3137
  median_household_income: 65959
  poverty_rate: 10.88
  homeownership_rate: 76.61
  unemployment_rate: 4.54
  median_home_value: 145700
  gini_index: 0.437
  vacancy_rate: 10.9
  race_white: 14488
  race_black: 1023
  race_asian: 110
  race_native: 196
  hispanic: 336
  bachelors_plus: 3523
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/senate/55"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/109"
    rel: in-district
    area_weight: 0.6776
  - to: "us/states/il/districts/house/110"
    rel: in-district
    area_weight: 0.3224
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Bond County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16716 |
| Under 18 | 2963 |
| 18–64 | 10616 |
| 65+ | 3137 |
| Median household income | 65959 |
| Poverty rate | 10.88 |
| Homeownership rate | 76.61 |
| Unemployment rate | 4.54 |
| Median home value | 145700 |
| Gini index | 0.437 |
| Vacancy rate | 10.9 |
| White | 14488 |
| Black | 1023 |
| Asian | 110 |
| Native | 196 |
| Hispanic/Latino | 336 |
| Bachelor's or higher | 3523 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 55](/us/states/il/districts/senate/55.md) — 100% (state senate)
- [IL House District 109](/us/states/il/districts/house/109.md) — 68% (state house)
- [IL House District 110](/us/states/il/districts/house/110.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

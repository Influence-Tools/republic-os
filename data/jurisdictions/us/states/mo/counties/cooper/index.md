---
type: Jurisdiction
title: "Cooper County, MO"
classification: county
fips: "29053"
state: "MO"
demographics:
  population: 16824
  population_under_18: 3750
  population_18_64: 9740
  population_65_plus: 3334
  median_household_income: 70625
  poverty_rate: 11.68
  homeownership_rate: 75.7
  unemployment_rate: 4.32
  median_home_value: 203500
  gini_index: 0.4061
  vacancy_rate: 14.44
  race_white: 14831
  race_black: 945
  race_asian: 21
  race_native: 17
  hispanic: 361
  bachelors_plus: 3765
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.9984
  - to: "us/states/mo/districts/senate/21"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/48"
    rel: in-district
    area_weight: 0.9649
  - to: "us/states/mo/districts/house/58"
    rel: in-district
    area_weight: 0.035
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Cooper County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16824 |
| Under 18 | 3750 |
| 18–64 | 9740 |
| 65+ | 3334 |
| Median household income | 70625 |
| Poverty rate | 11.68 |
| Homeownership rate | 75.7 |
| Unemployment rate | 4.32 |
| Median home value | 203500 |
| Gini index | 0.4061 |
| Vacancy rate | 14.44 |
| White | 14831 |
| Black | 945 |
| Asian | 21 |
| Native | 17 |
| Hispanic/Latino | 361 |
| Bachelor's or higher | 3765 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 21](/us/states/mo/districts/senate/21.md) — 100% (state senate)
- [MO House District 48](/us/states/mo/districts/house/48.md) — 96% (state house)
- [MO House District 58](/us/states/mo/districts/house/58.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

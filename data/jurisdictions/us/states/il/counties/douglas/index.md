---
type: Jurisdiction
title: "Douglas County, IL"
classification: county
fips: "17041"
state: "IL"
demographics:
  population: 19751
  population_under_18: 4859
  population_18_64: 11213
  population_65_plus: 3679
  median_household_income: 77320
  poverty_rate: 8.47
  homeownership_rate: 76.9
  unemployment_rate: 2.53
  median_home_value: 150400
  gini_index: 0.4028
  vacancy_rate: 8.72
  race_white: 17512
  race_black: 282
  race_asian: 82
  race_native: 46
  hispanic: 1672
  bachelors_plus: 3742
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/house/101"
    rel: in-district
    area_weight: 0.8871
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.1129
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Douglas County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 19751 |
| Under 18 | 4859 |
| 18–64 | 11213 |
| 65+ | 3679 |
| Median household income | 77320 |
| Poverty rate | 8.47 |
| Homeownership rate | 76.9 |
| Unemployment rate | 2.53 |
| Median home value | 150400 |
| Gini index | 0.4028 |
| Vacancy rate | 8.72 |
| White | 17512 |
| Black | 282 |
| Asian | 82 |
| Native | 46 |
| Hispanic/Latino | 1672 |
| Bachelor's or higher | 3742 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 100% (state senate)
- [IL House District 101](/us/states/il/districts/house/101.md) — 89% (state house)
- [IL House District 102](/us/states/il/districts/house/102.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

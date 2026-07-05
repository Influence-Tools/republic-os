---
type: Jurisdiction
title: "Pike County, IL"
classification: county
fips: "17149"
state: "IL"
demographics:
  population: 14469
  population_under_18: 3353
  population_18_64: 7964
  population_65_plus: 3152
  median_household_income: 59777
  poverty_rate: 14.85
  homeownership_rate: 77.65
  unemployment_rate: 3.94
  median_home_value: 101400
  gini_index: 0.4331
  vacancy_rate: 17.98
  race_white: 13808
  race_black: 87
  race_asian: 41
  race_native: 1
  hispanic: 298
  bachelors_plus: 2382
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/50"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/house/100"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Pike County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14469 |
| Under 18 | 3353 |
| 18–64 | 7964 |
| 65+ | 3152 |
| Median household income | 59777 |
| Poverty rate | 14.85 |
| Homeownership rate | 77.65 |
| Unemployment rate | 3.94 |
| Median home value | 101400 |
| Gini index | 0.4331 |
| Vacancy rate | 17.98 |
| White | 13808 |
| Black | 87 |
| Asian | 41 |
| Native | 1 |
| Hispanic/Latino | 298 |
| Bachelor's or higher | 2382 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 100% (congressional)
- [IL Senate District 50](/us/states/il/districts/senate/50.md) — 100% (state senate)
- [IL House District 100](/us/states/il/districts/house/100.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

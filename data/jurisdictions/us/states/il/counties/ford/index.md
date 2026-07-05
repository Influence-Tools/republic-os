---
type: Jurisdiction
title: "Ford County, IL"
classification: county
fips: "17053"
state: "IL"
demographics:
  population: 13406
  population_under_18: 3130
  population_18_64: 7648
  population_65_plus: 2628
  median_household_income: 62439
  poverty_rate: 12.42
  homeownership_rate: 72.29
  unemployment_rate: 5.46
  median_home_value: 122000
  gini_index: 0.4342
  vacancy_rate: 6.95
  race_white: 12111
  race_black: 71
  race_asian: 55
  race_native: 4
  hispanic: 707
  bachelors_plus: 2322
districts:
  - to: "us/states/il/districts/02"
    rel: in-district
    area_weight: 0.901
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.099
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.8098
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.1902
  - to: "us/states/il/districts/house/106"
    rel: in-district
    area_weight: 0.8098
  - to: "us/states/il/districts/house/101"
    rel: in-district
    area_weight: 0.1902
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Ford County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13406 |
| Under 18 | 3130 |
| 18–64 | 7648 |
| 65+ | 2628 |
| Median household income | 62439 |
| Poverty rate | 12.42 |
| Homeownership rate | 72.29 |
| Unemployment rate | 5.46 |
| Median home value | 122000 |
| Gini index | 0.4342 |
| Vacancy rate | 6.95 |
| White | 12111 |
| Black | 71 |
| Asian | 55 |
| Native | 4 |
| Hispanic/Latino | 707 |
| Bachelor's or higher | 2322 |

## Districts

- [IL-02](/us/states/il/districts/02.md) — 90% (congressional)
- [IL-16](/us/states/il/districts/16.md) — 10% (congressional)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 81% (state senate)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 19% (state senate)
- [IL House District 106](/us/states/il/districts/house/106.md) — 81% (state house)
- [IL House District 101](/us/states/il/districts/house/101.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries

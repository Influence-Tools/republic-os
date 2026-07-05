---
type: Jurisdiction
title: "Campbell County, KY"
classification: county
fips: "21037"
state: "KY"
demographics:
  population: 93426
  population_under_18: 19222
  population_18_64: 57827
  population_65_plus: 16377
  median_household_income: 77567
  poverty_rate: 11.1
  homeownership_rate: 71.08
  unemployment_rate: 3.98
  median_home_value: 252000
  gini_index: 0.4765
  vacancy_rate: 6.73
  race_white: 84891
  race_black: 2631
  race_asian: 891
  race_native: 47
  hispanic: 2449
  bachelors_plus: 36416
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/ky/districts/senate/24"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/ky/districts/house/68"
    rel: in-district
    area_weight: 0.6458
  - to: "us/states/ky/districts/house/78"
    rel: in-district
    area_weight: 0.2242
  - to: "us/states/ky/districts/house/67"
    rel: in-district
    area_weight: 0.1289
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Campbell County, KY

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 93426 |
| Under 18 | 19222 |
| 18–64 | 57827 |
| 65+ | 16377 |
| Median household income | 77567 |
| Poverty rate | 11.1 |
| Homeownership rate | 71.08 |
| Unemployment rate | 3.98 |
| Median home value | 252000 |
| Gini index | 0.4765 |
| Vacancy rate | 6.73 |
| White | 84891 |
| Black | 2631 |
| Asian | 891 |
| Native | 47 |
| Hispanic/Latino | 2449 |
| Bachelor's or higher | 36416 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 24](/us/states/ky/districts/senate/24.md) — 100% (state senate)
- [KY House District 68](/us/states/ky/districts/house/68.md) — 65% (state house)
- [KY House District 78](/us/states/ky/districts/house/78.md) — 22% (state house)
- [KY House District 67](/us/states/ky/districts/house/67.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
